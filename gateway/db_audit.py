import sqlalchemy_json_audit as audit

def enable(engine):
    """Enable JSON audit logging on the given SQLAlchemy engine."""
    return audit.install(engine)
