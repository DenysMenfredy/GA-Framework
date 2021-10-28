# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, String, TIMESTAMP, Table, Text, text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

Base = declarative_base()
metadata = Base.metadata


class Algorithm(Base):
    __tablename__ = 'algorithm'

    algorithm_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    algorithm_name = Column(String(64), nullable=False)
    short_name = Column(String(16))
    description = Column(Text, nullable=False)


class Datatype(Base):
    __tablename__ = 'datatype'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)

    Operators = relationship('Operator', secondary='operator_has_datatype')
    Problems = relationship('Problem', secondary='problem_has_datatype')


class Operator(Base):
    __tablename__ = 'operator'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    type = Column(String(16), nullable=False)
    description = Column(Text, nullable=False)


class Problem(Base):
    __tablename__ = 'problem'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    description = Column(Text, nullable=False)


class Function(Problem):
    __tablename__ = 'function'

    Problem_id = Column(ForeignKey('problem.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, index=True)
    minimumDimension = Column(Integer, nullable=False)
    maximumDimension = Column(Integer, nullable=False)
    upperBound = Column(Float, nullable=False)
    lowerBound = Column(Float, nullable=False)
    globalOptimum = Column(Float)
    maximization = Column(Boolean, nullable=False)


class Selection(Base):
    __tablename__ = 'selection'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    description = Column(Text, nullable=False)


class Status(Base):
    __tablename__ = 'status'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, unique=True)
    description = Column(String(256), nullable=False)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    login = Column(String(64), nullable=False, unique=True)
    password = Column(String(64), nullable=False)
    name = Column(String(64), nullable=False)
    notification_email = Column(String(64), nullable=False)


class Execution(Base):
    __tablename__ = 'execution'

    id = Column(Integer, primary_key=True)
    User_id = Column(ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    Algorithm_id = Column(ForeignKey('algorithm.algorithm_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    Status_id = Column(ForeignKey('status.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    Problem_id = Column(ForeignKey('problem.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    seed = Column(Float(asdecimal=True), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    finished_at = Column(TIMESTAMP)
    Selection_id = Column(ForeignKey('selection.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    Mutation_id = Column(ForeignKey('operator.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    Crossover_id = Column(ForeignKey('operator.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    Algorithm = relationship('Algorithm')
    Crossover = relationship('Operator', primaryjoin='Execution.Crossover_id == Operator.id')
    Mutation = relationship('Operator', primaryjoin='Execution.Mutation_id == Operator.id')
    Problem = relationship('Problem')
    Selection = relationship('Selection')
    Status = relationship('Status')
    User = relationship('User')


t_operator_has_datatype = Table(
    'operator_has_datatype', metadata,
    Column('Operator_id', ForeignKey('operator.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('DataType_id', ForeignKey('datatype.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_problem_has_datatype = Table(
    'problem_has_datatype', metadata,
    Column('Problem_id', ForeignKey('problem.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('DataType_id', ForeignKey('datatype.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)
)