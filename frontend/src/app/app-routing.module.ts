import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './views/home/home.component';
import { VotacaoFinalizadaComponent } from './views/votacao-finalizada/votacao-finalizada.component';
import { CriarVotacaoComponent } from './views/criar-votacao/criar-votacao.component';
import { VotacaoAndamentoComponent } from './views/votacao-andamento/votacao-andamento.component';
import { VotacaoIniciarComponent } from './views/votacao-iniciar/votacao-iniciar.component';

const routes: Routes = [

  { path: 'home', component: HomeComponent },
  { path: '', component: HomeComponent },
  { path: 'votacao-finalizada', component: VotacaoFinalizadaComponent},
  { path: 'criar-votacao', component: CriarVotacaoComponent},
  { path: 'votacao-andamento', component: VotacaoAndamentoComponent},
  { path: 'votacao-iniciar', component: VotacaoIniciarComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { relativeLinkResolution: 'legacy' })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
