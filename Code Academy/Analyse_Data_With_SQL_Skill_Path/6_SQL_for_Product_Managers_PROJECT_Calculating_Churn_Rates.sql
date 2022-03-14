with months as (
  select
  ‘2017-01-01’ as first_day,
  ‘2017-01-31’ as last_day
  union
  select
  ‘2017-02-01’ as first_day,
  ‘2017-02-28’ as last_day
  union
  select
  ‘2017-03-01’ as first_day,
  ‘2017-03-31’ as last_day
),

cross_join as (
  select *
  from subscriptions
  cross join months
),

status as (
  select
    id,
    first_day as month,
    segment,
    case
      when (segment = 87)
      (subscription_start < first_day)
      and (subscription_end > first_day
      or subscription_end is null) then 1
      else 0
      end as is_active_87,
    case
      when (segment = 30)
      and (subscription_start < first_day)
      and (subscription_end > first_day
      or subscription_end is null) then 1
      else 0
      end as is_active_30),
    case
      when (segment = 87)
      and (subscription_end between first_day and last_day) then 1
      else 0
      end as is_canceled_87,
    case
      when (segment = 30)
      and (subscription_end between first_day and last_day) then 1
      else 0
      end as is_canceled_30,
  from cross_join
  ),

status_aggregate as (
  select
  month,
  sum(is_active_87) as sum_active_87,
  sum(is_active_30) as sum_active_30,
  sum(is_canceled_87) as sum_canceled_87,
  sum(is_canceled_30) as sum_canceled_30
  from status
  group by month, segment
)

select *
from status
limit 10;
