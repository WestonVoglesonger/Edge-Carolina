import { Component, Input } from "@angular/core";
import { ProductService } from "../products.service";
import { ProductData } from "../productdata";
import { Router } from "@angular/router";
import { MatCardModule } from "@angular/material/card";

@Component({
  selector: "product-widget",
  templateUrl: "./product.widget.html",
  styleUrls: ["./product.widget.css"],
})
export class ProductWidget {
  /** Product this widget is showing. */
  @Input() productData!: ProductData;

  constructor(
    private productService: ProductService,
    private router: Router,
  ) {}

  /** Navigates to the product edit page */
  editProduct() {
    this.router.navigate(["/product/edit", this.productData.id]);
  }

  /** Deletes the current product */
  deleteProduct() {
    this.productService.deleteProduct(this.productData.id).subscribe(() => {
      this.productService.getProducts();
    });
  }
}
