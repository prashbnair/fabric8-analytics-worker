# you are doing it right celery:
#   ImportError: No module named celery
#
from cucoslib.workers.anitya import AnityaTask
from cucoslib.workers.binwalk import BinwalkTask
from cucoslib.workers.bigquery_gh import BigQueryTask
from cucoslib.workers.code_metrics import CodeMetricsTask
from cucoslib.workers.csmock_worker import CsmockTask
from cucoslib.workers.CVEchecker import CVEcheckerTask
from cucoslib.workers.snyk import SnykSyncTask
from cucoslib.workers.dependency_snapshot import DependencySnapshotTask
from cucoslib.workers.digester import DigesterTask
from cucoslib.workers.license import LicenseCheckTask
from cucoslib.workers.linguist import LinguistTask
from cucoslib.workers.manifest_keeper import ManifestKeeperTask
from cucoslib.workers.mercator import MercatorTask
from cucoslib.workers.githuber import GithubTask
from cucoslib.workers.githuber import GitReadmeCollectorTask
from cucoslib.workers.graph_importer import GraphImporterTask
from cucoslib.workers.graph_sync import GraphSyncTask
from cucoslib.workers.oscryptocatcher import OSCryptoCatcherTask
from cucoslib.workers.blackduck import BlackDuckLatentCollector
from cucoslib.workers.blackduck import BlackDuckTask
from cucoslib.workers.downstream import DownstreamUsageTask
from cucoslib.workers.finalize import FinalizeTask
from cucoslib.workers.graphaggregator import GraphAggregatorTask
from cucoslib.workers.stackaggregator import StackAggregatorTask
from cucoslib.workers.recommender import RecommendationTask
from cucoslib.workers.init import InitAnalysisFlow
from cucoslib.workers.init import FinishedAnalysisGateTask
from cucoslib.workers.result_collector import ResultCollector
