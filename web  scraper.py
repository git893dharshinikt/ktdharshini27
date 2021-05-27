import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect

parser=argparse.ArgumentParser{}
parser.add_argument("--page_num_max_", help="enter the number of pages to parse",type=int)
parser.add_argument("dbname", help="enter the number of pages to parse",type=int)
args=parser.parse_args()

oyo_url="https://www.oyorooms.com/hotels-in-bangalore/?page="
page_num_max=args.page_num_max
scraped_info_list=[]
connect.connect(dbname)

for page_num in range(1,page_num_max):
    req=requests.get(oyo_url+str(page_num))
    content=req.content

    soup=BeautifulSoup(content,"hml.parser")

    all_hotels=soup.find_all("div",{"class":"hotelcardlisting"})

    for hotel in all_hotels:
        hotel_dict={}
        hotel_dict["name"]=hotel.find("h3",{"class":"listingHotelDescription_hotelName"}).text
        hotel_dict["address"]=hotel.find("span",{"itemprop":"streetAddress"}).text
        hotel_dict["price"]=hotel.find("span",{"class":"listingPrice_finalPrice"}).text

        try:
             hotel_dict["rating"]=hotel.find("span",{"class":"hotelRating_ratingSummary"}).text
        expect AttributeError:
            pass

        parent_amenities_element=hotel.find("div",{"class":"amenityWrapper"}).text

        amenities_list=[]
        for amenity in  parent_amenities_element.find_all("div",{"class":"amenityWrapper_amenity"}):
            amentities_list.append(amenity.find("span",{"class":"d-body-sm"}).text.string())

        hotel_dict{"amenities"}=','.join(amenities_list[:-1])

        scraped_info_list.append(hotel_dict)
        connect.insert_into_table(args.dbname,tuple(hotel_dict.value())

dataFrame=pandas.DataFrame(scraped_info_list)
dataFrame.to_csv("oyo.csv")
connect.get_hotel_info(args.dbname)
 
        

            

       
