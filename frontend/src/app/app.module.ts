import { CUSTOM_ELEMENTS_SCHEMA, ErrorHandler, LOCALE_ID, NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { defineLocale, ptBrLocale } from 'ngx-bootstrap/chronos';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { registerLocaleData } from '@angular/common';

defineLocale('pt-br', ptBrLocale);
import localeBr from '@angular/common/locales/pt';
import { HomeComponent } from './views/home/home.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
registerLocaleData(localeBr, 'pt');

import { CarouselModule } from 'ngx-bootstrap/carousel';
import { FormsModule } from '@angular/forms';
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';
import { NgxSpinnerModule } from 'ngx-spinner';
import { CarregandoService } from './services/carregamento/carregamento.service';
import { ApplicationInterceptorHandler } from './app-interceptor-handler';
import { AmbienteServiceProvider } from './services/base/ambiente.service.provider';
import { SharedModule } from './components/shared.module';
import { ToastrModule } from 'ngx-toastr';
import { VotacaoFinalizadaComponent } from './views/votacao-finalizada/votacao-finalizada.component';
import { ModalModule } from 'ngx-bootstrap/modal';
import { CriarVotacaoComponent } from './views/criar-votacao/criar-votacao.component';
import { VotacaoAndamentoComponent } from './views/votacao-andamento/votacao-andamento.component';
import { VotacaoIniciarComponent } from './views/votacao-iniciar/votacao-iniciar.component';

declare module "@angular/core" {
  interface ModuleWithProviders<T = any> {
    ngModule: Type<T>;
    providers?: Provider[];
  }
}

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    VotacaoFinalizadaComponent,
    CriarVotacaoComponent,
    VotacaoAndamentoComponent,
    VotacaoIniciarComponent
  ],
  schemas: [ CUSTOM_ELEMENTS_SCHEMA ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    FormsModule,
    HttpClientModule,
    CarouselModule.forRoot(),
    SharedModule,
    NgxSpinnerModule,
    ToastrModule.forRoot(),
    ModalModule.forRoot(),
  ],
  providers: [CarregandoService, {provide: LOCALE_ID, useValue: 'pt'},
    { provide: ErrorHandler, useClass: ApplicationInterceptorHandler },
    { provide: HTTP_INTERCEPTORS, useClass: ApplicationInterceptorHandler, multi: true },
    AmbienteServiceProvider
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
