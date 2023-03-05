GET Message: 
    curl http://127.0.0.1:8080/all --http0.9
POST Message:
    curl -X POST http://127.0.0.1:8080/add/samsung -d '{"model":"S21","color":"pink","year":"2022","price":"860"}' --http0.9