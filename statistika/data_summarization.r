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

#penggabungan berdasarkan kolom

data_c <- select(data_a,c(order_id,segment,sub_category,sales))%>% head(9)

data_d <- select(data_b,c(order_id,segment,sub_category,category,order_date))

bind_cols(data_c,data_b)

#join/ menggabungkan yg sama
inner_join(data_c,data_d)

full_join(data_c,data_d)

left_join(data_c,data_d)