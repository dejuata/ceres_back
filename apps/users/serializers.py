from rest_framework import serializers
from apps.authentication.models import User
from rest_framework.exceptions import ErrorDetail, ValidationError
from rest_framework.utils import html, model_meta, representation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'id_card', 'role', 'phone', 'birthdate')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 6}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        # raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)
        if not instance.password == password:
            instance.set_password(password)

        m2m_fields = []
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            else:
                setattr(instance, attr, value)

        instance.save()
        for attr, value in m2m_fields:
            field = getattr(instance, attr)
            field.set(value)
        return instance

    def is_valid(self, raise_exception=False):
        initial_data_copy = self.initial_data.copy()
        if not initial_data_copy.get('password', False) and self.instance:
            initial_data_copy['password'] = self.instance.password
        assert hasattr(self, 'initial_data'), (
            'Cannot call `.is_valid()` as no `data=` keyword argument was '
            'passed when instantiating the serializer instance.'
        )

        if not hasattr(self, '_validated_data'):
            try:
                self._validated_data = self.run_validation(initial_data_copy)
            except ValidationError as exc:
                self._validated_data = {}
                self._errors = exc.detail
            else:
                self._errors = {}

        if self._errors and raise_exception:
            raise ValidationError(self.errors)

        return not bool(self._errors)
