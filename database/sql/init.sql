CREATE TABLE IF NOT EXISTS cart_items (
    user_id VARCHAR NOT NULL,
    product_id VARCHAR NOT NULL,
    quantity INTEGER NOT NULL,
    PRIMARY KEY (user_id, product_id)
);


CREATE TABLE IF NOT EXISTS product_catalogue (
    product_id VARCHAR NOT NULL,
    PRIMARY KEY (product_id)
);
