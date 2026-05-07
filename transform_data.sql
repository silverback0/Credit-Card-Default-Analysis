SELECT 
    MIN(age) as youngest, 
    MAX(age) as oldest, 
    AVG(credit_limit) as avg_limit
FROM v_cleaned_credit_analysis;