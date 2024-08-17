import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("Keys.json")

firebase_admin.initialize_app(cred, {

    'databaseURL':""
})

ref = db.reference("students")

data = {
        "1DS22IS136":
        {
            "Name":"Shambhav Kumar",
            "Subject":"Physics",
            "total_attendance":8,
            "Semester":4,
            "last_attendance_time":"2024-07-11 00:54:34"

        },
         "1DS22IS133":
        {
            "Name":"Sarvochcha Sharma",
            "Subject":"Physics",
            "total_attendance":8,
            "Semester":4,
            "last_attendance_time":"2024-07-11 00:54:34"

        }, "1DS22IS165":
        {
            "Name":"Sunny Kumar",
            "Subject":"Physics",
            "total_attendance":8,
            "Semester":4,
            "last_attendance_time":"2024-07-11 00:54:34"

        },
         "1DS22IS184":
        {
            "Name":"Vishesh Kumar",
            "Subject":"Physics",
            "total_attendance":8,
            "Semester":4,
            "last_attendance_time":"2024-07-11 00:54:34"

        },
         "1DS22CG045":
        {
            "Name":"King",
            "Subject":"Physics",
            "total_attendance":8,
            "Semester":4,
            "last_attendance_time":"2024-07-11 00:54:34"

        }




}

for key, value in data.items():
    ref.child(key).set(value)