mongo -- "$MONGO_INITDB_DATABASE" <<EOF
    db.createCollection('$MONGO_INITDB_COLLECTION');
EOF