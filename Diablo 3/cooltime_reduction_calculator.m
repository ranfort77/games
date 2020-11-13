clear all; clc; close all;

status = 999;

switch status
    case 1 % ��Ʈ + ũ����
        % 0.9431: 3���簨���� ��; ũ���� ��
        % 0.9330: ��� ��
        paragon = 0.1;
        helm    = 0.47;
        gems    = 0.125 * 3;
        ring    = 0.47;
        amulet  = 0.47;
        gokok   = 0.15;
        kremson = 0.20;
    case 2 % ����
        % 0.9288: 3���簨���� ��; ũ���� ��
        % 0.9163: ��� ��
        paragon = 0.1;
        helm    = 0.47;
        gems    = 0.125 * 3;
        ring    = 0.47;
        amulet  = 0.47;
        gokok   = 0.15;
        kremson = 0.00;        
    case 3
        % 0.8496: 3���簨���� ��; ũ���� ��
        % 0.8230: ��� ��
        paragon = 0.1;
        helm    = 0.00;
        gems    = 0.125 * 1;
        ring    = 0.47;
        amulet  = 0.47;
        gokok   = 0.15;
        kremson = 0.20;       
    case 4
        % 0.8120: 3���簨���� ��; ũ���� ��
        % 0.7788: ��� ��
        paragon = 0.1;
        helm    = 0.00;
        gems    = 0.125 * 1;
        ring    = 0.47;
        amulet  = 0.47;
        gokok   = 0.15;
        kremson = 0.00;    
    case 999  % test
        paragon = 0.0;
        helm    = 0.00;
        gems    = 0.125 * 0;
        ring    = 0.10;
        amulet  = 0.08;
        gokok   = 0.00;
        kremson = 0.00;          
end



% ---------------------------------------------------------------------
reductions = [paragon, helm, gems, ring, amulet, gokok, kremson];

total = 1 - prod(1 - reductions)


