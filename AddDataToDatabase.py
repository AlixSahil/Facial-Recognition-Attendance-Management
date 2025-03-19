import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("facial-rec-attendance-firebase-adminsdk-i5i4p-453401aa38.json")
firebase_admin.initialize_app(cred,{
'databaseURL': "https://facial-rec-attendance-default-rtdb.firebaseio.com/"

})

ref = db.reference('Student')

data = {
    "40021":
        {
            "name": "Sahil Ali ",
            "department": "MCA",
            "starting_year":2023,
            "total_attendance":10,
            "standing": "G",
            "year":2,
            "last_attendance_time": "2024-03-26 01:02:34"
        },
    "40026":
        {
            "name": "Sneha Kumari ",
            "department": "MCA",
            "starting_year":2023,
            "total_attendance":10,
            "standing": "G",
            "year":2,
            "last_attendance_time": "2024-03-26 01:02:34"
        },
    "40038":
        {
            "name": "Arif Irfan Khan ",
            "department": "MCA",
            "starting_year":2023,
            "total_attendance":10,
            "standing": "G",
            "year":2,
            "last_attendance_time": "2024-03-26 01:02:34"
        }

}

for Key,value in data.items():
    ref.child(Key).set(value)