from graphene import Schema

# QUERIES AND MUTATIONS
from .data.orders.orders_schema import Query as OrderQuery, Mutation as OrderMutation
from .data.products.products_schema import Query as ProductQuery, Mutation as ProductMutation
from .data.products.order_product_schema import Query as OrderProductQuery, Mutation as OrderProductMutation
from .data.notifications.notifications_schema import Query as NotificationQuery, Mutation as NotificationMutation
from .data.users.users_schema import Query as UserQuery, Mutation as UserMutation
from .data.profiles.profiles_schema import Query as ProfileQuery, Mutation as ProfileMutation
from .data.categories.categories_schema import Query as CategoryQuery, Mutation as CategoryMutation


class Query(ProfileQuery, UserQuery, OrderQuery, NotificationQuery, OrderProductQuery, ProductQuery, CategoryQuery):
    pass


class Mutation(ProfileMutation, UserMutation, OrderMutation, ProductMutation, OrderProductMutation, CategoryMutation,
               NotificationMutation):
    pass


ROOT_SCHEMA = Schema(query=Query, mutation=Mutation)
