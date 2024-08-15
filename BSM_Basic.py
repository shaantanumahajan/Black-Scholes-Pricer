import math
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, option_type='call'):
    """
    Parameters:
    S : float : Current stock price
    K : float : Strike price
    T : float : Time to maturity (in years)
    r : float : Risk-free interest rate (annualized)
    sigma : float : Volatility of the underlying asset (annualized)
    option_type : str : 'call' for call option, 'put' for put option

    Returns:
    float : Option price
    """
    
    # Calculate d1 and d2
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    
    if option_type == 'call':
        # Call option price
        option_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        # Put option price
        option_price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")
    
    return option_price

def get_float_input(prompt):
    """Function to get valid float input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_option_type():
    """Function to get valid option type ('call' or 'put') from the user."""
    while True:
        option_type = input("Enter option type ('call' or 'put'): ").strip().lower()
        if option_type in ['call', 'put']:
            return option_type
        else:
            print("Invalid option type. Please enter 'call' or 'put'.")

def main():
    print("Black-Scholes Option Pricing Model\n")
    
    S = get_float_input("Enter the current stock price (S): ")
    K = get_float_input("Enter the strike price (K): ")
    T = get_float_input("Enter the time to maturity in years (T): ")
    r = get_float_input("Enter the risk-free interest rate (r) as a decimal (e.g., 0.05 for 5%): ")
    sigma = get_float_input("Enter the volatility (sigma) as a decimal (e.g., 0.2 for 20%): ")
    option_type = get_option_type()

    # Calculate and display the option price
    option_price = black_scholes(S, K, T, r, sigma, option_type)
    print(f"\nThe {option_type} option price is: {option_price:.2f}")

if __name__ == "__main__":
    main()
