import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";
import { HomeComponent } from "./home/home.component";
import { AboutComponent } from "./about/about.component";
import { JoinComponent } from "./join/join.component";
import { ProductsComponent } from "./products/products.component";

const routes: Routes = [
  HomeComponent.Route,
  AboutComponent.Route,
  JoinComponent.Route,
  ProductsComponent.Route,
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
