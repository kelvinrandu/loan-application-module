import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService]
})
export class AppComponent {
  banks = [{bank_name: 'kcb', branch_name: 'parklands'},{bank_name: 'barclays', branch_name: 'westlands'}];

  constructor(private api: ApiService ){
    this.getAllBanks();
  }
  getAllBanks = () => {
    this.api.getAllBanks().subscribe(
      data => {
        this.banks = data;

      },
      error => {
        console.log(error);
      }
    )

  }
}
