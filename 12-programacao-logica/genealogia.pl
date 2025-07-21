% Fatos: Definindo os indivíduos e seus sexos
homem(joao).
homem(pedro).
homem(carlos).
mulher(ana).
mulher(maria).
mulher(laura).
mulher(teresa).

% Fatos: Definindo as relações de progenitor(Pai/Mãe, Filho/Filha)
progenitor(joao, pedro).
progenitor(maria, pedro).
progenitor(joao, ana).
progenitor(maria, ana).
progenitor(pedro, carlos).
progenitor(laura, carlos).
progenitor(pedro, teresa).
progenitor(laura, teresa).

% --- REGRAS ---

% Regra para definir 'pai'
pai(X, Y) :- progenitor(X, Y), homem(X).

% Regra para definir 'mãe'
mae(X, Y) :- progenitor(X, Y), mulher(X).

% Regra para definir 'filho'
filho(X, Y) :- progenitor(Y, X), homem(X).

% Regra para definir 'avô'
avo(X, Z) :- pai(X, Y), progenitor(Y, Z).

% Regra para definir 'irmão' ou 'irmã'
irmao(X, Y) :-
    pai(Pai, X), pai(Pai, Y),
    mae(Mae, X), mae(Mae, Y),
    X \= Y.