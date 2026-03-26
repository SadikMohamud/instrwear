erDiagram
    USER {
        int id PK
        string email
        string password
        string first_name
        string last_name
        enum role
        datetime date_joined
    }

    MERCHANTPROFILE {
        int id PK
        int user_id FK
        string store_name
        string description
        string location
        bool verified
    }

    CATEGORY {
        int id PK
        string name
        string description
    }

    PRODUCT {
        int id PK
        int merchant_id FK
        int category_id FK
        string name
        string description
        decimal price
        int stock
        string image
    }

    ORDER {
        int id PK
        int user_id FK
        decimal total_price
        enum status
        datetime created_at
    }

    ORDERITEM {
        int id PK
        int order_id FK
        int product_id FK
        int quantity
        decimal price
    }

    CART {
        int id PK
        int user_id FK
    }

    CARTITEM {
        int id PK
        int cart_id FK
        int product_id FK
        int quantity
    }

    USER ||--o{ MERCHANTPROFILE : has
    USER ||--o{ ORDER : places
    USER ||--o{ CART : owns

    MERCHANTPROFILE ||--o{ PRODUCT : sells
    PRODUCT }o--|| CATEGORY : belongs_to

    ORDER ||--o{ ORDERITEM : contains
    PRODUCT ||--o{ ORDERITEM : included_in

    CART ||--o{ CARTITEM : has
    PRODUCT ||--o{ CARTITEM : added_to