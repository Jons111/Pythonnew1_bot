from aiogram.dispatcher.filters.state import State,StatesGroup

class Forma(StatesGroup):
    ism_qabul = State()
    fam_qabul = State()
    yosh_qabul = State()
    nomer_qabul = State()
    manzil_qabul = State()
    taqqoslash =State()
    wikipedia=State()
    adminga_murojat= State()