from unittest import skip, TestCase

from adapters.video import MysqlVideoRepository
from tests.core.adapters.video import VideoRepositoryContractTest


@skip('NOT IMPLEMENTED')
class MysqlVideoRepositoryContractTest(TestCase, VideoRepositoryContractTest):

    def setUp(self):
        self.repo = MysqlVideoRepository()