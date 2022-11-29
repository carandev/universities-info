
from sqlalchemy.orm import Session
from config.database import db_engine
from scraper.udes_data import get_UDES_data
from scraper.udi_data import get_UDI_data
from scraper.uis_data import get_UIS_data
from scraper.unab_data import get_UNAB_data
from scraper.upb_data import get_UPB_data
from scraper.uts_data import get_UTS_data


def careers_to_db():
    with Session(db_engine) as session:
        session.execute("SET FOREIGN_KEY_CHECKS=0")
        session.execute("DELETE FROM universities")
        session.execute("DELETE FROM careers")
        session.execute("SET FOREIGN_KEY_CHECKS=1")

        udes = get_UDES_data()
        udi = get_UDI_data()
        uis = get_UIS_data()
        upb = get_UPB_data()
        uts = get_UTS_data()
        unab = get_UNAB_data()
        session.add_all([udes, udi, uis, upb, uts, unab])

        session.commit()
