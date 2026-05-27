from app import db


class Office(db.Model):
    __tablename__ = "offices"

    officeCode = db.Column(db.String, primary_key=True)
    city = db.Column(db.String)
    state = db.Column(db.String)
    country = db.Column(db.String)

    employees = db.relationship("Employee", backref="office")


class Employee(db.Model):
    __tablename__ = "employees"

    employeeNumber = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String)
    lastName = db.Column(db.String)
    jobTitle = db.Column(db.String)

    officeCode = db.Column(
        db.String,
        db.ForeignKey("offices.officeCode")
    )


class Customer(db.Model):
    __tablename__ = "customers"

    customerNumber = db.Column(db.Integer, primary_key=True)
    customerName = db.Column(db.String)
    contactFirstName = db.Column(db.String)
    contactLastName = db.Column(db.String)
    phone = db.Column(db.String)
    creditLimit = db.Column(db.Float)

    salesRepEmployeeNumber = db.Column(
        db.Integer,
        db.ForeignKey("employees.employeeNumber")
    )


class Order(db.Model):
    __tablename__ = "orders"

    orderNumber = db.Column(db.Integer, primary_key=True)
    customerNumber = db.Column(
        db.Integer,
        db.ForeignKey("customers.customerNumber")
    )


class OrderDetail(db.Model):
    __tablename__ = "orderdetails"

    orderNumber = db.Column(
        db.Integer,
        db.ForeignKey("orders.orderNumber"),
        primary_key=True
    )

    productCode = db.Column(
        db.String,
        primary_key=True
    )

    quantityOrdered = db.Column(db.Integer)


class Product(db.Model):
    __tablename__ = "products"

    productCode = db.Column(db.String, primary_key=True)
    productName = db.Column(db.String)


class Payment(db.Model):
    __tablename__ = "payments"

    customerNumber = db.Column(
        db.Integer,
        db.ForeignKey("customers.customerNumber"),
        primary_key=True
    )

    checkNumber = db.Column(db.String, primary_key=True)
    paymentDate = db.Column(db.String)
    amount = db.Column(db.String)