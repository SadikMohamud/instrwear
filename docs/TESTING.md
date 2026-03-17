# Testing

## Manual Testing

| Feature               | Expected Outcome                  | Result |
|----------------------|----------------------------------|--------|
| Registration         | User account created             | Pass   |
| Login                | User logs in                     | Pass   |
| Merchant Profile     | Profile created                  | Pass   |
| Stripe Payment       | Payment processed successfully   | Pass   |
| Payment Confirmation | Confirmation displayed           | Pass   |

---

## Stripe Testing

| Test Case           | Expected Outcome              | Result |
|--------------------|------------------------------|--------|
| Valid payment      | Payment succeeds             | Pass   |
| Invalid card       | Payment rejected             | Pass   |
| Cancel payment     | User redirected correctly    | Pass   |

---

## Tawk.to AI Assistant Testing

| Feature            | Expected Outcome                    | Result |
|-------------------|------------------------------------|--------|
| Chat loads        | Visible on customer pages           | Pass   |
| AI response       | Provides relevant answers           | Pass   |
| Role restriction  | Hidden from merchant views          | Pass   |

---

## Validation

- Django form validation implemented
- Model constraints enforced
- Server-side validation applied

---

## Known Issues

- No real-time delivery tracking
- UI interactivity can be further enhanced