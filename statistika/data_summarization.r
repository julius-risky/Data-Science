dataset %>% group_by(segment,category) %>% summarise(total_sale=sum(sales),avg_sales=mean(sales),min_quantity=min(quantity),max_quantity=max(quantity),n_order=n())

#penggabungan data frame

data_a <- dataset %>% filter(segment=='Corporate') %>%
  select(order_id,order_date,segment,category,sub_category,sales)%>%
  head(10)


data_b <- dataset %>% filter(category=='Technology') %>%
  select(order_id,order_date,segment,category,sub_category,sales)%>%
  head(9)

intersect(data_a,data_b)

setdiff(data_a,data_b)
