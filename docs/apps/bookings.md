# Models

## bookings

### Booking

Fields:

- `identifier`: Unique identifier for the print request.
- `description`: A short text description of the booking request.
- `original_cost`: Total cost of the service before any discounts.
- `discount`: Amount of discount applied to the original cost.
- `amount_to_pay`: Total cost of the service after applying the discount.
- `status`: Current status of the request (e.g., "pending", "accepted", "printing", "completed", "denied").
- `is_paid`: A boolean indicating whether the payment has been received from the customer.
- `method_of_payment`: Customer's method of payment (e.g., "cash", "gcash", "maya", "none").
- `checksum`: Ensures uniqueness by verifying file content to prevent duplicate entries.
- `are_files_deleted`: A boolean indicating whether the files associated with this request have been deleted from the server.
- `date_added`: The date and time when the request was added to the database.
- `date_modified`: The date and time when the request was last modified.
- `date_soft_deleted`: The date when the request was soft-deleted (if applicable).
- `expected_delivery_time`: The expected date and time the customer wants to receive the service (nullable and blank).

#### identifier

The `identifier` field is used to store a unique identifier for each print request. This identifier consists of a combination of lower case ASCII characters and numerical digits, totaling 36 possible characters.

To generate this unique identifier, a function called `generate_unique_identifier` is used. This function takes an optional `length` parameter (defaulting to 5) and creates a random identifier by selecting characters from the set of lower case letters and digits. The result is a unique identifier consisting of the specified number of characters.

The first 3 characters of the identifier represent the index, incrementing with each new booking totaling 46656 unique booking request entries. The remaining 2 characters are randomized to prevent predictable booking IDs.

### UploadedFile

Fields:

- `booking`: Foreign Key to the corresponding `Booking` for this file.
- `file`: The uploaded file.
- `description`: Additional information about the file.
- `status`: Current status of the file (e.g., "pending", "printing", "printed").

### FilePage

Fields:

- `file`: Foreign Key to `Booking.UploadedFile`.
- `quantity`: Number of quantity to be printed for the selected pages.
- `color`: Color setting for printing (e.g., "black and white", "full color").
- `quality`: Print quality (e.g., "High Quality", "Standard")
- `paper_type`: A text field for the paper type (customers can input the paper they want)
- `pages`: List of page numbers to be printed with the specified settings.
- `comment`: A short comment text field.
