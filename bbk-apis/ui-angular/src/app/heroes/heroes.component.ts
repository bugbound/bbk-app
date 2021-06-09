import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Hero } from '../core';
import { ScanService } from './scan.service';

@Component({
  selector: 'app-heroes',
  templateUrl: './heroes.component.html'
})
export class HeroesComponent implements OnInit {
  selected: Hero;
  heroes$: Observable<Hero[]>;
  message = '?';
  heroToDelete: Hero;
  showModal = false;

  constructor(private scanService: ScanService) {
    this.heroes$ = scanService.entities$;
  }

  ngOnInit() {
    this.getHeroes();
  }

  add(hero: Hero) {
    this.scanService.add(hero);
  }

  askToDelete(hero: Hero) {
    this.heroToDelete = hero;
    this.showModal = true;
    if (this.heroToDelete.name) {
      this.message = `Would you like to delete ${this.heroToDelete.name}?`;
    }
  }

  clear() {
    this.selected = null;
  }

  closeModal() {
    this.showModal = false;
  }

  deleteHero() {
    this.closeModal();
    if (this.heroToDelete) {
      this.scanService
        .delete(this.heroToDelete.id)
        .subscribe(() => (this.heroToDelete = null));
    }
    this.clear();
  }

  enableAddMode() {
    this.selected = <any>{};
  }

  getHeroes() {
    this.scanService.getAll();
    this.clear();
  }

  save(hero: Hero) {
    if (this.selected && this.selected.name) {
      this.update(hero);
    } else {
      this.add(hero);
    }
  }

  select(hero: Hero) {
    this.selected = hero;
  }

  update(hero: Hero) {
    this.scanService.update(hero);
  }
}
