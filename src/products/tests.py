from django.test import TestCase
from .models import Category, Manufacturer, Product
from .serializers import CategorySerializer, ManufacturerSerializer, ProductSerializer

# Create your tests here.

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(category_name="Electronics")

    def test_category_creation(self):
        self.assertIsInstance(self.category, Category)
        self.assertEqual(self.category.category_name, "Electronics")
        self.assertIsNotNone(self.category.created_At)
        self.assertIsNotNone(self.category.updated_At)

class ManufacturerModelTest(TestCase):
    def setUp(self):
        self.manufacturer = Manufacturer.objects.create(
            manufacturer_name="Acme Corp",
            email="contact@acme.com",
            phone_number="123456789",
            location="Tema"
        )

    def test_manufacturer_creation(self):
        self.assertIsInstance(self.manufacturer, Manufacturer)
        self.assertEqual(self.manufacturer.manufacturer_name, "Acme Corp")
        self.assertEqual(self.manufacturer.email, "contact@acme.com")
        self.assertEqual(self.manufacturer.phone_number, "123456789")
        self.assertEqual(self.manufacturer.location, "Tema")
        self.assertIsNotNone(self.manufacturer.created_At)
        self.assertIsNotNone(self.manufacturer.updated_At)

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(category_name="Electronics")
        self.manufacturer = Manufacturer.objects.create(
            manufacturer_name="Acme Corp",
            email="contact@acme.com",
            phone_number="123456789",
            location="Tema"
        )
        self.product = Product.objects.create(
            product_name="Smartphone",
            manufacturer_id=self.manufacturer,
            category_id=self.category,
            inventory=100,
            price=299.99
        )

    def test_product_creation(self):
        self.assertIsInstance(self.product, Product)
        self.assertEqual(self.product.product_name, "Smartphone")
        self.assertEqual(self.product.manufacturer_id, self.manufacturer)
        self.assertEqual(self.product.category_id, self.category)
        self.assertEqual(self.product.inventory, 100)
        self.assertEqual(self.product.price, 299.99)
        self.assertIsNotNone(self.product.created_At)
        self.assertIsNotNone(self.product.updated_At)



class CategorySerializerTest(TestCase):
    def setUp(self):
        self.category_data = {
            'category_name': 'Electronics'
        }
        self.category = Category.objects.create(**self.category_data)
        self.serializer = CategorySerializer(instance=self.category)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'category_name', 'created_At', 'updated_At'])

    def test_category_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['category_name'], self.category_data['category_name'])

class ManufacturerSerializerTest(TestCase):
    def setUp(self):
        self.manufacturer_data = {
            'manufacturer_name': 'Acme Corp',
            'email': 'contact@acme.com',
            'phone_number': '123456789',
            'location': 'Tema'
        }
        self.manufacturer = Manufacturer.objects.create(**self.manufacturer_data)
        self.serializer = ManufacturerSerializer(instance=self.manufacturer)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'manufacturer_name', 'email', 'phone_number', 'location', 'created_At', 'updated_At'])

    def test_manufacturer_field_content(self):
        data = self.serializer.data
        for key in self.manufacturer_data.keys():
            self.assertEqual(data[key], self.manufacturer_data[key])

class ProductSerializerTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(category_name='Electronics')
        self.manufacturer = Manufacturer.objects.create(
            manufacturer_name='Acme Corp',
            email='contact@acme.com',
            phone_number='123456789',
            location='Tema'
        )
        self.product_data = {
            'product_name': 'Smartphone',
            'manufacturer_id': self.manufacturer,
            'category_id': self.category,
            'inventory': 100,
            'price': 299.99
        }
        self.product = Product.objects.create(**self.product_data)
        self.serializer = ProductSerializer(instance=self.product)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'product_name', 'manufacturer_id', 'category_id', 'inventory', 'price'])

    def test_product_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['product_name'], self.product_data['product_name'])
        self.assertEqual(data['manufacturer_id']['manufacturer_name'], self.manufacturer.manufacturer_name)
        self.assertEqual(data['category_id']['category_name'], self.category.category_name)
        self.assertEqual(data['inventory'], self.product_data['inventory'])
        self.assertEqual(data['price'], self.product_data['price'])

    def test_product_creation(self):
        product_serializer = ProductSerializer(data={
            'product_name': 'Laptop',
            'manufacturer_id': self.manufacturer.id,
            'category_id': self.category.id,
            'inventory': 50,
            'price': 799.99
        })
        self.assertTrue(product_serializer.is_valid())
        product = product_serializer.save()
        self.assertEqual(product.product_name, 'Laptop')
        self.assertEqual(product.manufacturer, self.manufacturer)
        self.assertEqual(product.category, self.category)
        self.assertEqual(product.inventory, 50)
        self.assertEqual(product.price, 799.99)
