# MY BANKING WORLD (MBW)
 MY BANKING WORLD (MBW) is a Python-based banking management system designed to handle basic banking operations and account management for administrative use. The project includes features for creating, viewing, and managing various account types, including savings and current accounts.

## Project Structure
The project is organized as follows:
```
MY BANKING WORLD (MBW)
├── main.py                   # Main entry point to run the application
├── config
│   └── config.py             # Configuration settings (e.g., constants, paths, initial setup)
├── controllers               # Controllers to manage interactions between models, views, and services
├── exceptions
│   └── exceptions.py         # Custom exception classes for error handling across the app
├── models
│   ├── account.py            # Base class for common account properties and methods
│   ├── savings.py            # Savings account class with specific rules and methods
│   └── current.py            # Current account class with specific rules and methods
├── repositories
│   └── account_repository.py  # Handles account data storage and retrieval (in-memory or persistent)
├── resources
│   └── messages.py           # Stores messages, prompts, and any static text for reuse
├── services
│   ├── account_manager.py     # Manages account creation, deletion, and modifications
│   ├── account_privileges_manager.py  # Manages account privilege levels and access control
│   └── transaction_manager.py # Handles all account transactions (deposits, withdrawals, etc.)
├── tests
│   └── test_account_manager.py # Unit tests for account management functionality
├── utils                     # Utility functions and helper modules for common operations
└── views
    └── account_ui.py         # User interface logic for account operations and interactions
```
