# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, String, TIMESTAMP, Table, Text, text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

from sqlalchemy.sql.operators import as_

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

    datatype_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    datatype_name = Column(String(32), nullable=False)

    Operators = relationship('Operator', secondary='operator_has_datatype')
    Problems = relationship('Problem', secondary='problem_has_datatype')


class Operator(Base):
    __tablename__ = 'operator'

    operator_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    operator_name = Column(String(32), nullable=False)
    operator_type = Column(String(16), nullable=False)
    description = Column(Text, nullable=False)


class Problem(Base):
    __tablename__ = 'problem'

    problem_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    problem_name = Column(String(64), nullable=False)
    description = Column(Text, nullable=False)


class Function(Problem):
    __tablename__ = 'function'

    function_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    problem_id = Column(ForeignKey('problem.problem_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, index=True)
    minimum_dimension = Column(Integer, nullable=False)
    maximum_dimension = Column(Integer, nullable=False)
    upper_bound = Column(Float, nullable=False)
    lower_bound = Column(Float, nullable=False)
    optimum = Column(Float)
    maximization = Column(Boolean, nullable=False)


class Selection(Base):
    __tablename__ = 'selection'

    selection_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    selection_name = Column(String(32), nullable=False)
    description = Column(Text, nullable=False)

class Parameter(Base):
    __tablename__ = 'parameter'

    parameter_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    parameter_name = Column(String(32), nullable=False)
    description = Column(Text, nullable=False)


class Crossover(Base):
    __tablename__ = 'crossover'

    crossover_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    crossover_rate = Column(Float, nullable=False)

    parameter_id = Column(ForeignKey('parameter.parameter_id', ondelete='CASCADE', \
                          onupdate='CASCADE'), index=True)

class Mutation(Base):
    __tablename__ = 'mutation'

    mutation_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    mutation_rate = Column(Float, nullable=False)

    parameter_id = Column(ForeignKey('parameter.parameter_id', ondelete='CASCADE', \
                          onupdate='CASCADE'), index=True)
    


class Status(Base):
    __tablename__ = 'status'

    status_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    status_name = Column(String(32), nullable=False, unique=True)
    description = Column(String(256), nullable=False)


class User(Base):
    __tablename__ = 'user'

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String(64), nullable=False, unique=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False, unique=True)
    company = Column(String(64), nullable=True)


class Execution(Base):
    __tablename__ = 'execution'

    execution_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(ForeignKey('user.user_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    Algorithm_id = Column(ForeignKey('algorithm.algorithm_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    status_id = Column(ForeignKey('status.status_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    problem_id = Column(ForeignKey('problem.problem_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    seed = Column(Float(asdecimal=True), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    finished_at = Column(TIMESTAMP)
    selection_id = Column(ForeignKey('selection.selection_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    mutation_id = Column(ForeignKey('mutation.mutation_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    crossover_id = Column(ForeignKey('crossover.crossover_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    #TODO: fix execution has operators, many to many relationship
    Algorithm = relationship('Algorithm')
    Crossover = relationship('Crossover', primaryjoin='Execution.crossover_id == Crossover.crossover_id')
    Mutation = relationship('Mutation', primaryjoin='Execution.mutation_id == Mutation.mutation_id')
    Problem = relationship('Problem')
    Selection = relationship('Selection')
    Status = relationship('Status')
    User = relationship('User')


t_operator_has_datatype = Table(
    'operator_has_datatype', metadata,
    Column('Operator_id', ForeignKey('operator.operator_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('DataType_id', ForeignKey('datatype.datatype_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_problem_has_datatype = Table(
    'problem_has_datatype', metadata,
    Column('Problem_id', ForeignKey('problem.problem_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('DataType_id', ForeignKey('datatype.datatype_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)
)