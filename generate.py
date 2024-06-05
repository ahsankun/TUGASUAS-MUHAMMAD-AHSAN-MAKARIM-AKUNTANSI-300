import pandas as pd
import random
from faker import Faker

def generate_data(num_records=50):
    # Initialize Faker
    fake = Faker()

    # Seed for reproducibility
    Faker.seed(0)
    random.seed(0)

    # Generate data
    data = {
        "id": range(1, num_records + 1),
        "umur": [random.randint(18, 65) for _ in range(num_records)],
        "gaji": [random.randint(3000000, 20000000) for _ in range(num_records)],
        "gender": [random.choice(['Laki-laki', 'Perempuan']) for _ in range(num_records)],
        "pendidikan": [random.choice(['SD', 'SMP', 'SMA', 'S1', 'S2', 'S3']) for _ in range(num_records)],
        "rumah": [random.choice(['Ya', 'Tidak']) for _ in range(num_records)]
    }

    # Create DataFrame
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = generate_data()
    # Save the generated data to a CSV file
    df.to_csv("generated_data.csv", index=False)
    print("Data generated and saved to 'generated_data.csv'.")


