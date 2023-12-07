import { NgxSpinnerModule } from 'ngx-spinner';
import { ApplicationInterceptorHandler } from './../app-interceptor-handler';
import { CarregandoService } from './../services/carregamento/carregamento.service';
import { HTTP_INTERCEPTORS } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { LoadingComponent } from './loading/loading.component';
import { NgModule, ModuleWithProviders, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { CommonModule } from '@angular/common';
import { defineLocale } from 'ngx-bootstrap/chronos';
import { ptBrLocale } from 'ngx-bootstrap/locale';
defineLocale('pt-br', ptBrLocale);
import { registerLocaleData } from '@angular/common';
import localeBr from '@angular/common/locales/pt';
registerLocaleData(localeBr, 'pt');
import { BsDatepickerModule, BsLocaleService } from 'ngx-bootstrap/datepicker';



@NgModule({
  declarations: [
    LoadingComponent
  ],
  schemas: [ CUSTOM_ELEMENTS_SCHEMA ],
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    NgxSpinnerModule,
    BsDatepickerModule.forRoot(),
  ],
  exports: [
    CommonModule,
    ReactiveFormsModule,
    LoadingComponent,
    NgxSpinnerModule,
    BsDatepickerModule
  ]
})
export class SharedModule {

  constructor(private bsLocaleService: BsLocaleService) {
    this.bsLocaleService.use('pt-br');
  }

  static forRoot(): ModuleWithProviders<SharedModule> {
    return {
      ngModule: SharedModule,
      providers: [ CarregandoService, { provide: HTTP_INTERCEPTORS, useClass: ApplicationInterceptorHandler, multi: true }]
    };
  }
 }
