from rest_framework import viewsets, permissions
from .models import Report, Flag, Ban, Warning
from .serializers import ReportSerializer, FlagSerializer, BanSerializer, WarningSerializer
from .permissions import IsAdminOrReadOnly

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)


class FlagViewSet(viewsets.ModelViewSet):
    queryset = Flag.objects.all()
    serializer_class = FlagSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BanViewSet(viewsets.ModelViewSet):
    queryset = Ban.objects.all()
    serializer_class = BanSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]


class WarningViewSet(viewsets.ModelViewSet):
    queryset = Warning.objects.all()
    serializer_class = WarningSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]
