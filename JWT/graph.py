from flask import Flask
from flask_graphql import GraphQLView
import graphene


class User(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()


users = [
    User(id=1, name='Alice'),
    User(id=2, name='Bob'),
    User(id=3, name='Charlie'),
]

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return users

# Create a schema
schema = graphene.Schema(query=Query)

app = Flask(__name__)

app.add_url_rule(  '/graphql',view_func=GraphQLView.as_view( 'graphql',  schema=schema, graphiql=True ))

if __name__ == '__main__':
    app.run(debug=True)
