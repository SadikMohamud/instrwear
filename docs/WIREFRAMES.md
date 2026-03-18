# InstrWear Mid-Fidelity Wireframes

## Usage Notes
- Fidelity: Mid
- Grid: 12-column desktop, 4-column mobile
- Header and primary navigation remain consistent per role.
- Components are named to map to templates.

---

## 1) Landing Page
Template: templates/pages/landing.html

### Desktop Wireframe
```
+----------------------------------------------------------------------------------+
| LOGO                              [Features] [How It Works] [Log In]             |
+----------------------------------------------------------------------------------+
| HERO LEFT                                 | HERO RIGHT                            |
| Eyebrow Badge                             | Abstract Shape Stack                  |
| H1: Fashion Delivered In Minutes          | Floating Category Icons               |
| Paragraph                                 |                                        |
| [Start Shopping] [List Your Store]        |                                        |
+----------------------------------------------------------------------------------+
| Stats Bar: [500+ Stores] [15min] [50K+] [4.9]                                   |
+----------------------------------------------------------------------------------+
| Why InstrWear (6 feature cards in 3x2 grid)                                      |
+----------------------------------------------------------------------------------+
| How It Works Tabs: [Shoppers] [Merchants]                                         |
| Step Cards 1-4 (active tab content)                                               |
+----------------------------------------------------------------------------------+
| CTA Banner: Headline + 2 CTA buttons                                              |
+----------------------------------------------------------------------------------+
| Footer: Brand | Platform Links | Accounts Links | Project Links                  |
+----------------------------------------------------------------------------------+
```

### Mobile Wireframe
```
+--------------------------------+
| LOGO                 [Menu]    |
+--------------------------------+
| Hero Badge                     |
| H1                             |
| Paragraph                      |
| [Start Shopping]               |
| [List Your Store]              |
+--------------------------------+
| Stats (2x2 cards)              |
+--------------------------------+
| Features (stacked cards)       |
+--------------------------------+
| Tabs + Steps (stacked)         |
+--------------------------------+
| CTA + Footer links             |
+--------------------------------+
```

---

## 2) Login Page
Template: templates/accounts/login.html

### Desktop
```
+----------------------------------------------------------+
| Brand top-left                                           |
|                                                          |
|                +------------------------------+          |
|                | Login Card                   |          |
|                | Email                        |          |
|                | Password                     |          |
|                | [Log In]                     |          |
|                | Link: Register               |          |
|                +------------------------------+          |
+----------------------------------------------------------+
```

### Mobile
```
+------------------------------+
| Brand                        |
| Login Card                   |
| Email                        |
| Password                     |
| [Log In]                     |
| Register Link                |
+------------------------------+
```

---

## 3) Register Choice Page
Template: templates/accounts/register_choice.html

### Desktop
```
+----------------------------------------------------------------+
| Header                                                         |
+----------------------------------------------------------------+
|                 Choose Account Type                            |
|    +----------------------+    +----------------------+        |
|    | Shopper Card         |    | Merchant Card        |        |
|    | brief benefits       |    | brief benefits       |        |
|    | [Register Shopper]   |    | [Register Merchant]  |        |
|    +----------------------+    +----------------------+        |
+----------------------------------------------------------------+
```

### Mobile
```
+------------------------------+
| Choose Account Type          |
| Shopper card + CTA           |
| Merchant card + CTA          |
+------------------------------+
```

---

## 4) Register Shopper Page
Template: templates/accounts/register_shopper.html

### Desktop
```
+----------------------------------------------------------------+
| Header                                                         |
+----------------------------------------------------------------+
|                 Shopper Registration Form                       |
| First Name | Last Name                                          |
| Email                                                         |
| Password | Confirm Password                                     |
| Terms checkbox                                                  |
| [Create Shopper Account]                                        |
| Link: Already have account                                      |
+----------------------------------------------------------------+
```

### Mobile
```
+------------------------------+
| Shopper Register             |
| First Name                   |
| Last Name                    |
| Email                        |
| Password                     |
| Confirm Password             |
| Terms                        |
| [Create Account]             |
+------------------------------+
```

---

## 5) Register Merchant Page
Template: templates/accounts/register_merchant.html

### Desktop
```
+----------------------------------------------------------------+
| Header                                                         |
+----------------------------------------------------------------+
|                 Merchant Registration Form                      |
| First Name | Last Name                                          |
| Business Email                                                  |
| Password | Confirm Password                                     |
| Business Terms checkbox                                         |
| [Create Merchant Account]                                       |
+----------------------------------------------------------------+
```

### Mobile
```
+------------------------------+
| Merchant Register            |
| First Name                   |
| Last Name                    |
| Email                        |
| Password                     |
| Confirm Password             |
| [Create Account]             |
+------------------------------+
```

---

## 6) Merchant Onboarding Page
Template: templates/merchant/onboarding.html

### Desktop
```
+--------------------------------------------------------------------------------+
| Merchant Header                                                                |
+--------------------------------------------------------------------------------+
| Profile Setup Card                                                             |
| Business Name                                                                  |
| Phone                                                                          |
| Address: House | Street | City | County | Postcode                            |
| Bio                                                                            |
| Logo Upload                                                                    |
| [Save and Continue]                                                            |
+--------------------------------------------------------------------------------+
```

### Mobile
```
+--------------------------------+
| Merchant Onboarding            |
| Business Name                  |
| Phone                          |
| Address fields                 |
| Bio                            |
| Logo Upload                    |
| [Save and Continue]            |
+--------------------------------+
```

---

## 7) Merchant Dashboard Page
Template: templates/merchant/dashboard.html

### Desktop
```
+--------------------------------------------------------------------------------+
| Merchant Topbar: Brand | Nav | Profile                                         |
+--------------------------------------------------------------------------------+
| KPIs: [Total Products] [Active] [Low Stock] [Inventory Value]                  |
+--------------------------------------------------------------------------------+
| Left: Quick Add Product Form                | Right: Recent Products           |
| Name, Price, Stock, Category, Image         | Product table/cards              |
| [Add Product]                                | [Edit] [Delete]                 |
+--------------------------------------------------------------------------------+
```

### Mobile
```
+--------------------------------+
| Merchant Topbar                |
| KPI cards (2x2)                |
| Quick Add Product form         |
| Recent products stacked        |
+--------------------------------+
```

---

## 8) Merchant Products Page
Template: templates/merchant/products.html

### Desktop
```
+--------------------------------------------------------------------------------+
| Header + actions [Add Product]                                                 |
+--------------------------------------------------------------------------------+
| Filter/sort row                                                                 |
+--------------------------------------------------------------------------------+
| Product Grid/Table                                                              |
| [Image] [Name] [Category] [Price] [Stock] [Status] [Actions]                  |
| Actions: [View] [Delete]                                                       |
+--------------------------------------------------------------------------------+
```

### Mobile
```
+--------------------------------+
| Products + [Add]               |
| Filter/Sort                    |
| Product cards stacked          |
| Actions per card               |
+--------------------------------+
```

---

## 9) Add Product Page
Template: templates/merchant/add_product.html

### Desktop
```
+--------------------------------------------------------------------------------+
| Back to Products                                                                |
+--------------------------------------------------------------------------------+
| Add Product Card                                                                |
| Category                                                                        |
| Product Name                                                                    |
| Description                                                                     |
| Price | Stock                                                                   |
| Image Upload Dropzone                                                           |
| Active Toggle                                                                   |
| [Create Product]                                                                |
+--------------------------------------------------------------------------------+
```

### Mobile
```
+--------------------------------+
| Add Product                    |
| Category                       |
| Name                           |
| Description                    |
| Price                          |
| Stock                          |
| Upload Image                   |
| Active Toggle                  |
| [Create Product]               |
+--------------------------------+
```

---

## 10) Shopper Onboarding Page
Template: templates/shopper/onboarding.html

### Desktop
```
+--------------------------------------------------------------------------------+
| Shopper Header                                                                  |
+--------------------------------------------------------------------------------+
| Personal Setup Form                                                             |
| First Name | Last Name                                                          |
| Phone                                                                            |
| Address fields                                                                   |
| Profile Image Upload                                                             |
| [Save and Continue]                                                              |
+--------------------------------------------------------------------------------+
```

### Mobile
```
+--------------------------------+
| Shopper Onboarding             |
| Name fields                    |
| Phone                          |
| Address fields                 |
| Profile Image                  |
| [Save and Continue]            |
+--------------------------------+
```

---

## 11) Shopper Dashboard Page
Template: templates/shopper/dashboard.html

### Desktop
```
+--------------------------------------------------------------------------------+
| Shopper Topbar: Search | Cart Icon | Profile                                    |
+--------------------------------------------------------------------------------+
| Welcome + quick stats (orders, saved, etc.)                                     |
+--------------------------------------------------------------------------------+
| Recommended Products Carousel/Grid                                               |
+--------------------------------------------------------------------------------+
| Recent Orders Snapshot                                                           |
| [Browse Products] [Go to Orders]                                                 |
+--------------------------------------------------------------------------------+
```

### Mobile
```
+--------------------------------+
| Topbar + Cart                  |
| Welcome card                   |
| Product cards                  |
| Recent orders list             |
| Bottom nav                     |
+--------------------------------+
```

---

## 12) Shopper Product List Page
Template: templates/shopper/products_list.html

### Desktop
```
+--------------------------------------------------------------------------------+
| Topbar + Search + Cart Count                                                    |
+--------------------------------------------------------------------------------+
| Left Sidebar: Categories                    | Right: Product Grid              |
| Category links                               | Product Card x N                |
|                                               | Image, Name, Store, Price       |
|                                               | [Add to Cart] [Quick View]      |
+--------------------------------------------------------------------------------+
| Sort dropdown + pagination/fab                                                   |
+--------------------------------------------------------------------------------+
```

### Mobile
```
+--------------------------------+
| Search + Cart                  |
| Category chips                 |
| Sort dropdown                  |
| Product cards (single column)  |
| Bottom nav + back-to-top       |
+--------------------------------+
```

---

## 13) Product Detail Page
Template: templates/shopper/product_detail.html

### Desktop
```
+--------------------------------------------------------------------------------+
| Breadcrumb / Back to Shop                                                       |
+--------------------------------------------------------------------------------+
| Left: Product Image (large)              | Right: Product Info                |
|                                           | Category Badge                     |
|                                           | Name, Description                  |
|                                           | Price, Stock                       |
|                                           | [Add to Cart] [Back to Shop]       |
+--------------------------------------------------------------------------------+
```

### Mobile
```
+--------------------------------+
| Back to Shop                   |
| Product image                  |
| Category badge                 |
| Name                           |
| Description                    |
| Price + Stock                  |
| [Add to Cart]                  |
+--------------------------------+
```

---

## 14) Cart Page
Template: templates/shopper/cart.html

### Desktop
```
+--------------------------------------------------------------------------------+
| Cart Header (items count)                                                        |
+--------------------------------------------------------------------------------+
| Cart Items List                               | Order Summary                   |
| Item row: image, name, qty controls, price    | Subtotal                        |
| [Remove]                                       | Delivery                        |
|                                                | Total                           |
|                                                | [Proceed to Checkout]           |
+--------------------------------------------------------------------------------+
```

### Mobile
```
+--------------------------------+
| Cart (count)                   |
| Item card x N                  |
| Qty stepper + remove           |
| Summary card                   |
| [Proceed to Checkout]          |
+--------------------------------+
```

---

## 15) Checkout Page
Template: templates/shopper/checkout.html

### Desktop
```
+--------------------------------------------------------------------------------+
| Checkout Header                                                                  |
+--------------------------------------------------------------------------------+
| Left: Delivery Form                           | Right: Order Summary            |
| Full Name, Phone                               | Items + subtotal               |
| House, Street, City, County, Postcode          | Fees + total                   |
| [Pay with Stripe]                               | Security note                  |
+--------------------------------------------------------------------------------+
```

### Mobile
```
+--------------------------------+
| Checkout                       |
| Delivery fields                |
| Order summary                  |
| [Pay with Stripe]              |
+--------------------------------+
```

---

## 16) Checkout Success Page
Template: templates/shopper/checkout_success.html

### Desktop
```
+----------------------------------------------------------------+
| Success Icon + Confirmation                                     |
| Order number, summary, next steps                              |
| [View Orders] [Continue Shopping]                              |
+----------------------------------------------------------------+
```

### Mobile
```
+--------------------------------+
| Success                        |
| Order details                  |
| [View Orders]                  |
| [Continue Shopping]            |
+--------------------------------+
```

---

## 17) Orders Page
Template: templates/shopper/orders.html

### Desktop
```
+--------------------------------------------------------------------------------+
| Orders Header                                                                   |
+--------------------------------------------------------------------------------+
| Filters: status/date                                                            |
+--------------------------------------------------------------------------------+
| Order list/cards                                                                 |
| Order ID | Date | Items | Total | Payment Status | Fulfillment Status          |
| [Open details]                                                                   |
+--------------------------------------------------------------------------------+
```

### Mobile
```
+--------------------------------+
| Orders                         |
| Filter chips                   |
| Order cards stacked            |
| Status pills                   |
+--------------------------------+
```

---

## Wireframe Component Inventory
- Buttons: Primary, Secondary, Ghost
- Inputs: Text, Number, Select, Textarea, File Upload
- Status: Success, Error, Warning, Neutral
- Cards: Product Card, KPI Card, Summary Card
- Navigation: Header Nav, Bottom Nav (mobile shopper)

## Interaction Notes
- Primary CTA is always visually dominant.
- Destructive actions require confirmation state.
- Cart and checkout preserve context between screens.
- Merchant flows prioritize add/edit speed and stock visibility.

## Responsive Rules
- Desktop: sidebars and two-column compositions.
- Mobile: stacked cards, fixed bottom nav for shopper pages.
- Maintain touch targets at least 44px height.
