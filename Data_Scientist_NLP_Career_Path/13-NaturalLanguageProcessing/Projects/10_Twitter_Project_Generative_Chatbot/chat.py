import numpy as np
import re
from test_model import encoder_model, decoder_model, num_decoder_tokens, num_encoder_tokens, input_features_dict, target_features_dict, reverse_target_features_dict, max_decoder_seq_length, max_encoder_seq_length, decode_sequence

class ChatBot:
    negative_commands = ["no", "not really", "I don't want to", "no thanks"]
    exit_commands = ["exit", "quit", "bye", "goodbye"]

    def start_chat(self):
        print("Hello! Would you like to chat?")
        user_response = input()
        if any(neg in user_response for neg in self.negative_commands):
            print("Okay, have a great day!")
            return
        self.chat()

    def make_exit(self, reply):
        for exit_command in self.exit_commands:
            if exit_command in reply:
                print("Okay, have a great day!")
                return True
        return False

    def string_to_matrix(self, user_input):
        tokens = re.findall(r"[\w']+|[^\s\w]", user_input)
        user_input_matrix = np.zeros(
            (1, max_encoder_seq_length, num_encoder_tokens),
            dtype='float32')
        for timestep, token in enumerate(tokens):
            if token in input_features_dict:
                user_input_matrix[0, timestep, input_features_dict[token]] = 1.
        return user_input_matrix

    def generate_response(self, user_input):
        input_matrix = self.string_to_matrix(user_input)
        chatbot_response = decode_sequence(input_matrix)
        chatbot_response = chatbot_response.replace("<START>", "").replace("<END>", "")
        return chatbot_response

    def chat(self):
        reply = input()
        while not self.make_exit(reply):
            reply = input(self.generate_response(reply))

chatbot = ChatBot()
chatbot.start_chat()
