package com.nwachinemelu.bigdecimal;

import java.math.BigDecimal;

public class SimpleInterestCalculator {
	
	BigDecimal principal;
	BigDecimal interest;

	public SimpleInterestCalculator(String principal, String interest) {
		// TODO Auto-generated constructor stub
		this.principal= new BigDecimal(principal);
		this.interest= new BigDecimal(interest);
	}

	public BigDecimal calculateTotalValue(int noOfYears) {
		//total value=principal + principal*interest*noOfYears
		BigDecimal noOfYearsBigDecimal=new BigDecimal(noOfYears);
	
		BigDecimal totalValue= principal.add(
				
           principal.multiply(interest)
           .multiply(noOfYearsBigDecimal)                    
           );
		return totalValue;
	}

}
