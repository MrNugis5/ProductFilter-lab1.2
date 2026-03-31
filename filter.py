
class BetterFilter:
    """Better filter."""

    def filter(self, products, specification):
        """Filter products by specification."""
        for p in products:
            if specification.is_satisfied(p):
                yield p

    def filter_by_color(self, products, color):
        """Filter by color."""
        for p in products:
            if p.color == color:
                return p

    def filter_by_size(self, products, size):
        """Filter by size."""
        for p in products:
            if p.size == size:
                return p
