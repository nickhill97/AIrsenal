"""
fixtures that will be used by tests - e.g. a test database
"""

import pytest

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
Base = declarative_base()

from ..schema import Player, Match, Fixture, PlayerScore, PlayerPrediction

@pytest.fixture(scope='module')
def create_test_db():
    engine = create_engine("sqlite:////tmp/test.db")
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    session = DBSession()
    return session
