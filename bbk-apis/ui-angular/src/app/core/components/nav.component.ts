import { Component, OnInit } from '@angular/core';
// import { faCoffee } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-nav',
  template: `
  <nav class="menu">
    <p class="menu-label">Menu</p>
    <ul class="menu-list">
      <a routerLink="/scans" routerLinkActive="router-link-active">
        <span>Scans</span>
      </a>
      <a routerLink="/about" routerLinkActive="router-link-active">
        <span>About</span>
      </a>
    </ul>
  </nav>
  `
})
export class NavComponent implements OnInit {
  constructor() {}

  ngOnInit() {}
}
