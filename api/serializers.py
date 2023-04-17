from rest_framework import serializers

from book.models import Book, Author, BookInstance
from djoser.serializers import UserCreateSerializer


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']


# class GenreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Genre
#         fields = ['name']
#
#
# class LanguageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Language
#         fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()

    # genre = GenreSerializer
    # language = LanguageSerializer
    class Meta:
        model = Book
        fields = ('title', 'description', 'price', 'date_added', 'discount_price', 'author')

    author = serializers.HyperlinkedRelatedField(
        queryset=Author.objects.all(),
        view_name='author-detail',
        # lookup_field='id'
    )
    # date_added = serializers.DateTimeField(read_only=True)
    discount_price = serializers.SerializerMethodField(method_name='discount')

    def discount(self, book: Book):
        return book.price * 25 / 100


class BookCreateSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer

    # genre = GenreSerializer
    # language = LanguageSerializer

    class Meta:
        model = Book
        fields = ('title', 'isbn', 'description', 'genre', 'language', 'price', 'author', 'discount_price')

    # fields = ('title', 'isbn', 'description', 'author', 'genre', 'language')


# class AuthorSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=255)
#     last_name = serializers.CharField(max_length=255)
#
# #
class UserCreate(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']


class BookInstanceSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BookInstance
        fields = ['user_id', 'due_back', 'status', 'book', 'imprint', 'borrower']
