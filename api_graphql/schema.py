from graphene import Schema

#QUERIES AND MUTATIONS
from .data.orders.orders_schema import Query as OrderQuery#, Mutation as OrderMutation
from .data.products.products_schema import Query as ProductQuery, Mutation as ProductMutation
from .data.products.order_product_schema import Query as OrderProductQuery, Mutation as OrderProductMutation
from .data.notifications.notifications_schema import Query as NotificationQuery, Mutation as NotificationMutation
from .data.users.users_schema import Query as UserQuery#, Mutation as UserMutation





class Query(UserQuery,OrderQuery,NotificationQuery, OrderProductQuery,ProductQuery):    
    pass
    
class Mutation(ProductMutation,OrderProductMutation, NotificationMutation):
    pass
 

ROOT_SCHEMA= Schema(query=Query, mutation=Mutation)