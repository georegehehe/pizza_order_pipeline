DO $$
BEGIN
    CREATE TABLE states (
        state VARCHAR(50) PRIMARY KEY,
        population INT NOT NULL
    );

    CREATE TABLE customer (
        customer_id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL,
        city TEXT NOT NULL,
        state VARCHAR(50) REFERENCES states(state),
        zip_code VARCHAR(20) NOT NULL
    );


    CREATE TABLE orders(
        order_id INT PRIMARY KEY,
        customer_id INT REFERENCES customer(customer_id),
        type TEXT NOT NULL,
        quantity INT NOT NULL,
        price DECIMAL(3,2) NOT NULL,
        order_time TIMESTAMPTZ NOT NULL,
        state VARCHAR(50) REFERENCES states(state)
    );

END $$;