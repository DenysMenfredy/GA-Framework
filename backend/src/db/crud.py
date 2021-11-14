from uuid import uuid4
from sqlalchemy.orm import Session
from pydantic.types import UUID4
from . import models, schemas


#TODO: Implement all CRUD operations for the tables

def get_user_by_id(db: Session, user_id: UUID4):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def user_login(db: Session, login_request: schemas.Login):
    user = db.query(models.User).filter(models.User.username==login_request.username).first()
    if user:
        if user.password == login_request.password:
            return user
    return None

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserBase):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(username=user.username, first_name=user.first_name, \
                          last_name=user.last_name, email=user.email, 
                          password=fake_hashed_password, company=user.company)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_problem(db: Session, problem: schemas.ProblemBase):
    # problem_id = UUID()
    # print(problem_id)
    db_problem = models.Problem(problem_name=problem.problem_name, \
                                description=problem.description)
    db.add(db_problem)
    db.commit()
    db.refresh(db_problem)
    return db_problem

def get_problems(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Problem).offset(skip).limit(limit).all()


def get_functions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Function).\
              add_columns(models.Function.function_id,
                          models.Problem.problem_id,
                          models.Problem.problem_name,
                          models.Function.maximum_dimension,
                          models.Function.minimum_dimension,
                          models.Function.upper_bound,
                          models.Function.lower_bound,
                          models.Function.optimum,
                          models.Function.maximization,                        
                          models.Problem.description).\
              join(models.Problem).\
              offset(skip).\
              limit(limit).all()

def get_function_by_id(db: Session, function_id: UUID4):
    return db.query(models.Function).\
              add_columns(models.Function.function_id,
                          models.Problem.problem_id,
                          models.Problem.problem_name,
                          models.Function.maximum_dimension,
                          models.Function.minimum_dimension,
                          models.Function.upper_bound,
                          models.Function.lower_bound,
                          models.Function.optimum,
                          models.Function.maximization,                        
                          models.Problem.description).\
              join(models.Problem).\
              filter(models.Function.function_id == function_id).first()

def create_function(db: Session, function: schemas.FunctionCreate):
    db_function = models.Function(function_id = function.function_id, \
                                  problem_id = function.problem_id, \
                                  maximum_dimension=function.maximum_dimension, \
                                  minimum_dimension=function.minimum_dimension, \
                                  upper_bound=function.upper_bound, \
                                  lower_bound=function.lower_bound, \
                                  optimum=function.optimum, \
                                  maximization=function.maximization)
    db.add(db_function)
    db.commit()
    db.refresh(db_function)
    return db_function

def create_algorithm(db: Session, algorithm: schemas.AlgorithmBase):
    db_algorithm = models.Algorithm(algorithm_id = algorithm.algorithm_id, \
                                    algorithm_name=algorithm.algorithm_name, \
                                    short_name=algorithm.short_name, \
                                    description=algorithm.description)

    db.add(db_algorithm)
    db.commit()
    db.refresh(db_algorithm)
    return db_algorithm

def get_algorithms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Algorithm).offset(skip).limit(limit).all()

def get_algorithm(db: Session, algorithm_id: UUID4):
    return db.query(models.Algorithm).filter(models.Algorithm.algorithm_id == algorithm_id)\
             .first()
    
def create_parameter(db: Session, parameter: schemas.ParameterBase):
    db_parameter = models.Parameter(parameter_name=parameter.parameter_name, \
                                    description=parameter.description)
    db.add(db_parameter)
    db.commit()
    db.refresh(db_parameter)
    return db_parameter

def get_parameters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Parameter).offset(skip).limit(limit).all()

def get_parameter(db: Session, parameter_id: UUID4):
    return db.query(models.Parameter).filter(models.Parameter.parameter_id == parameter_id)\
             .first()

def create_status(db: Session, status: schemas.Status):
    db_status = models.Status(status_name=status.status_name, \
                              description=status.description)
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status

def get_status(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Status).offset(skip).limit(limit).all()

def get_selections(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Selection).offset(skip).limit(limit).all()

def create_selection(db: Session, selection: schemas.Selection):
    db_selection = models.Selection(selection_name=selection.selection_name, \
                                    description=selection.description)
    db.add(db_selection)
    db.commit()
    db.refresh(db_selection)
    return db_selection

def get_operators(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Operator).offset(skip).limit(limit).all()

def create_operator(db: Session, operator: schemas.Operator):
    db_operator = models.Operator(operator_name=operator.operator_name, \
                                  operator_type=operator.operator_type, \
                                  description=operator.description)
    db.add(db_operator)
    db.commit()
    db.refresh(db_operator)
    return db_operator

def get_crossovers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Crossover).\
              add_columns(models.Crossover.crossover_id,
                          models.Parameter.parameter_id,
                          models.Parameter.parameter_name,
                          models.Crossover.crossover_rate,
                          models.Parameter.description).\
              join(models.Parameter).\
              offset(skip).\
              limit(limit).all()


def create_crossover(db: Session, crossover: schemas.Crossover):
    db_crossover = models.Crossover(crossover_rate=crossover.crossover_rate, \
                                    parameter_id=crossover.parameter_id)
    db.add(db_crossover)
    db.commit()
    db.refresh(db_crossover)
    return db_crossover

def get_mutations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Mutation).\
              add_columns(models.Mutation.mutation_id, 
                          models.Parameter.parameter_id, 
                          models.Parameter.parameter_name, 
                          models.Mutation.mutation_rate, 
                          models.Parameter.description).\
              join(models.Parameter).\
              offset(skip).\
              limit(limit).all()

def create_mutation(db: Session, mutation: schemas.Mutation):
    db_mutation = models.Mutation(mutation_rate=mutation.mutation_rate, \
                                  parameter_id=mutation.parameter_id)
    db.add(db_mutation)
    db.commit()
    db.refresh(db_mutation)
    return db_mutation


def create_execution(db: Session, execution: schemas.Execution):
    db_execution = models.Execution(execution_id=execution.execution_id, \
                                    algorithm_id=execution.algorithm_id, \
                                    problem_id=execution.problem_id, \
                                    user_id=execution.user_id, \
                                    status_id=execution.status_id, \
                                    selection_id=execution.selection_id, \
                                    crossover_id=execution.crossover_id, \
                                    mutation_id=execution.mutation_id, \
                                    seed=execution.seed)
    db.add(db_execution)
    db.commit()
    db.refresh(db_execution)
    return db_execution

def get_executions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Execution).offset(skip).limit(limit).all()


def get_execution(db: Session, execution_id: UUID4):
    return db.query(models.Execution).filter(models.Execution.execution_id == execution_id)\
             .first()
                                        