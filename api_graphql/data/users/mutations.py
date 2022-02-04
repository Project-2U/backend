import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation
from users.models import User
from users.forms import UserModelForm
from profiles.models import UserProfile
from .types import UserType
from api_graphql.data.profiles.types import ProfileType
from graphene import Field, Mutation


class UserInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    lastname = graphene.String(required=True)
    age = graphene.Int()
    phone = graphene.String()
    address = graphene.String()
    occupation = graphene.String()
    email = graphene.String(required=True)
    password = graphene.String(required=True)


class UserMutation(Mutation):
    class Arguments:
        input = UserInput(required=True)

    user=Field(UserType)

    @staticmethod
    def mutate(root, info, input: UserInput):
        input = vars(input)
        name = input.get('name')
        lastname = input.get("lastname")
        age = input.get("age")
        phone = input.get('phone')
        address = input.get('address')
        occupation = input.get('occupation')
        email = input.get("email")
        password = input.get('password')
        profile = UserProfile.objects.create_user(email=email, password=password)
        obj = User.objects.create(lastname=lastname, age=age, phone=phone, address=address,
                                 occupation=occupation, user_profile_id=profile.id)
        return UserMutation(user=obj)

