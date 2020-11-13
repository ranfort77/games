clear all; clc; close all;

status = 999;

switch status
    case 1 % ¼¼Æ® + Å©¸²½¼
        % 0.9431: 3¼ÚÀç°¨Åõ±¸ À¯; Å©¸²½¼ À¯
        % 0.9330: °î¿Á ¹«
        paragon = 0.1;
        helm    = 0.47;
        gems    = 0.125 * 3;
        ring    = 0.47;
        amulet  = 0.47;
        gokok   = 0.15;
        kremson = 0.20;
    case 2 % ½ÇÃß
        % 0.9288: 3¼ÚÀç°¨Åõ±¸ À¯; Å©¸²½¼ ¹«
        % 0.9163: °î¿Á ¹«
        paragon = 0.1;
        helm    = 0.47;
        gems    = 0.125 * 3;
        ring    = 0.47;
        amulet  = 0.47;
        gokok   = 0.15;
        kremson = 0.00;        
    case 3
        % 0.8496: 3¼ÚÀç°¨Åõ±¸ ¹«; Å©¸²½¼ À¯
        % 0.8230: °î¿Á ¹«
        paragon = 0.1;
        helm    = 0.00;
        gems    = 0.125 * 1;
        ring    = 0.47;
        amulet  = 0.47;
        gokok   = 0.15;
        kremson = 0.20;       
    case 4
        % 0.8120: 3¼ÚÀç°¨Åõ±¸ ¹«; Å©¸²½¼ ¹«
        % 0.7788: °î¿Á ¹«
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


