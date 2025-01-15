from prefect import flow
#from tasks.task_prueba import task_prueba
from tasks.task_extract_link import task_extract_link
from tasks.task_transform_link import task_transform_link
from tasks.task_load_link import task_load_link

@flow(name="ETL Linkein_Offers")
def main_flow():
    #task_prueba()}
    #PASO 1 - EXTRAER DATA
    offer_lists = task_extract_link(skill)
    #PASO 2 - TRANSFORMAR DATA
    offer_lists_transform = task_transform_link(offer_lists)
    #PASO 3 - CARGAR DATA
    task_load_link(offer_lists_transform)

if __name__ == "__main__":
    skill = input('ingrese skill a buscar : ')
    main_flow()
    