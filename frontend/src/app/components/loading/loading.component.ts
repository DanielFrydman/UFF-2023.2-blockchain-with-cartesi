import { NgxSpinnerService } from 'ngx-spinner';
import { Component, OnInit } from '@angular/core';
import { Subject } from 'rxjs';
import { CarregandoService } from 'app/services/carregamento/carregamento.service';

@Component({
  selector: 'app-loading',
  templateUrl: './loading.component.html',
  styleUrls: ['./loading.component.css']
})
export class LoadingComponent {

  color = 'primary';
  mode = 'indeterminate';
  value = 90;
  isLoading: Subject<boolean> = this.servicoCarregamento.carregando$;

  constructor(private servicoCarregamento: CarregandoService, private spinner: NgxSpinnerService) {

    this.spinner.show();
  }


}
