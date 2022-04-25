from venv import create
from rest_framework import serializers
from consts import boards
from .models import Board, ModeratorInvitaion, Post, Thread


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = '__all__'

    def update(self, instance, validated_data):
        if "moderators" in validated_data:
            moderators = validated_data.pop("moderators")
            for moderator in moderators:
                invitaion = ModeratorInvitaion.objects.get_or_create(
                    board=instance.id,
                    user=moderator.id,
                )
                if invitaion.status == boards.INVIATION_STATUS_DECLINED:
                    invitaion.status = boards.INVIATION_STATUS_PENDING
                invitaion.save()
        return super().update(instance, validated_data)


class ModeratorInvitaionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ModeratorInvitaion
        fields = '__all__'

    def update(self, instance, validated_data):
        invitaion = ModeratorInvitaion.objects.get(
                    board=instance.board,
                    user=instance.user,
                    status=validated_data.pop("status")
        )
        invitaion.save()
        if invitaion.status == boards.INVITATION_STATUS_ACCETPED:
            board = Board.objects.get(id=instance.board.id)
            board.moderators.add(instance.user)
            board.save()
        return super().update(instance, validated_data)

class ThreadSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = '__all__'

class PostSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'