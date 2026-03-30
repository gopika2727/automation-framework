class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_btn = "#add-to-cart-sauce-labs-backpack"
        self.cart_icon = ".shopping_cart_link"

    def add_product_to_cart(self):
        self.page.click(self.add_to_cart_btn)

    def open_cart(self):
        self.page.click(self.cart_icon)